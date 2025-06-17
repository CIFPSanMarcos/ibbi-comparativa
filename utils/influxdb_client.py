import streamlit as st
from influxdb_client_3 import InfluxDBClient3, Point

host = st.secrets["INFLUX_HOST"]
org = st.secrets["INFLUX_ORG"]
token = st.secrets["INFLUX_TOKEN"]

client = InfluxDBClient3(host=host, token=token, org=org)

print(f'"Connected to InfluxDB at {host} with organization {org}"')
print(client)