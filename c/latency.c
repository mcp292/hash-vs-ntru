/* gcc latency.c -o latency && ./latency */

/* Single latency: 11337000 nano seconds
   Average latency: 9000521 nano seconds */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "keccak_fips202.c"

double calc_clock_time(double start, double stop)
{
    /* Returns difference in start, stop clock times in seconds.
       Automatically converts clock_t values to double. To be used with
       clock_t clock() of time.h. */
    return ((stop - start) / CLOCKS_PER_SEC);
}

double convert_to_nanoseconds(double clock_time)
{
    return clock_time * 1e9;
}

void hash_repeatedly(unsigned char input_bytes[], int num_bytes, int num_hashes)
{
    const int NUM_OUTPUT_BYTES = 32; /* sha256 -> 256 bits -> 32 bytes */

    int iter;
    unsigned char output_bytes[NUM_OUTPUT_BYTES];

    for (iter = 0; iter < num_hashes; iter++)
    {
        FIPS202_SHA3_256(input_bytes, num_bytes, output_bytes);
        memcpy(input_bytes, output_bytes, NUM_OUTPUT_BYTES);
    }
}

void hash_repeatedly_repeatedly(
    unsigned char input_bytes[], int num_bytes, int num_hashes, int num_times)
{
    int iter;

    for (iter = 0; iter < num_times; iter++)
    {
        hash_repeatedly(input_bytes, num_bytes, num_hashes);
    }
}

void get_rand_bytes(unsigned char bytes[], int num_bytes)
{
    int ind;

    srand(time(NULL));

    for (ind = 0; ind < num_bytes; ind++)
    {
        bytes[ind] = rand(); /* integer automatically truncated */
    }
}

int main()
{
    const int NUM_TIMES = 1000;
    const int NUM_HASHES = 1000;
    const int NUM_BITS = 256;
    const int NUM_BYTES = NUM_BITS / 8;

    clock_t start, stop;
    double clock_time, single_latency, avg_latency;
    unsigned char input_bytes[NUM_BYTES];

    printf("getting random bytes");
    get_rand_bytes(input_bytes, NUM_BYTES);
    printf("...finished\n");

    printf("single latency");
    start = clock();
    hash_repeatedly(input_bytes, NUM_BYTES, NUM_HASHES);
    stop = clock();
    printf("...finished\n");

    clock_time = calc_clock_time(start, stop);
    single_latency = convert_to_nanoseconds(clock_time);

    printf("avg latency");
    start = clock();
    hash_repeatedly_repeatedly(input_bytes, NUM_BYTES, NUM_HASHES, NUM_TIMES);
    stop = clock();
    printf("...finished\n\n");

    clock_time = calc_clock_time(start, stop);
    avg_latency = convert_to_nanoseconds(clock_time) / NUM_TIMES;

    printf("Single latency: %.0lf nano seconds\n", single_latency);
    printf("Average latency: %.0lf nano seconds\n", avg_latency);

    return 0;
}
