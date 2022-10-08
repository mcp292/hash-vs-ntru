import altair as alt
import pandas as pd

data = {"Function": ["SHA3-256 (C)",
                     "SHA3-256 (Python)",
                     "Polynomial Exponentiation Mod 2",
                     "Polymnomial Exponentiation Mod 3"],
        "Latency (nanoseconds)": [9000521,
                                  746765,
                                  0,
                                  0]}

df = pd.DataFrame(data)

chart = alt.Chart(df).mark_bar().encode(
    x="Function:N",
    y="Latency (nanoseconds):Q",
    color="Function:N"
).properties(
    width=150,
    title="Average Latency Over 1000 Iterations"
    # (hashed 1000 times, 1000 times and took the average latency)
)

chart.save("avg_latency_hash_vs_ntru.png", webdriver="firefox")
