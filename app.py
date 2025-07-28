import streamlit as st
import pandas as pd

st.title("Illinois Opponent Scouting Dashboard (2024–25)")

# Illinois team stats (public)
illini_or = 114.8
illini_dr = 102.7

st.subheader("Illinois 2024–25 Team Metrics")
st.write(f"- Offensive Rating: **{illini_or}**")
st.write(f"- Defensive Rating: **{illini_dr}**")

df = pd.read_csv("data/opponent_stats.csv")
selected = st.selectbox("Select Upcoming Opponent", df["Opponent"])

opp = df[df["Opponent"] == selected].iloc[0]
st.subheader(f"Opponent: {selected}")
st.write(f"- Adj. Offense: {opp.AdjO}")
st.write(f"- Adj. Defense: {opp.AdjD}")
st.write(f"- Tempo: {opp.Tempo}")
st.write(f"- Key Strength: {opp.KeyStrength}")

# Strategy suggestions
if opp.KeyStrength == "Elite Defense":
    st.info("Strategy: Attack mismatches and run pick-and-roll sets.")
elif opp.KeyStrength == "Elite Offense":
    st.info("Strategy: Slow the pace and emphasize transition defense.")
elif opp.KeyStrength == "Fast Pace":
    st.info("Strategy: Control the tempo and prevent fast breaks.")
else:
    st.info("Strategy: Balanced approach with execution in half-court sets.")
