import streamlit as st
from influxdb_client_3 import InfluxDBClient3, Point
from datetime import datetime, timedelta

def get_latest_data_from_influx(client, key):
    query = f"""SELECT "{key}", "time", "zona"
        FROM "energia"
        WHERE
        "{key}" IS NOT NULL
        AND "zona" IN ('zonaalta', 'zonabaja', 'zonamedia')
        ORDER BY time DESC
        LIMIT 1 """
    
    table = client.query(query=query, database="ibbi-influxdb", language='sql')

    # Convert to dataframe
    df = table.to_pandas().sort_values(by="time")

    return df

def query_data_from_influx(client, start_date, end_date, key):
    print(f"🔄 Cargando datos desde InfluxDB para el rango {start_date} → {end_date}...")
    query = f"""SELECT
        date_trunc('hour', time) AS hour,
        zona,
        avg({key}) AS {key}
        FROM
        "energia"
        WHERE
        time >= TIMESTAMP '{start_date}'
        AND time <= TIMESTAMP '{end_date}'
        AND {key} IS NOT NULL
        AND zona IN ('zonaalta', 'zonabaja', 'zonamedia')
        GROUP BY
        hour, zona
        ORDER BY
        hour, zona """

    table = client.query(query=query, database="ibbi-influxdb", language='sql')

    # Convert to dataframe
    df = table.to_pandas()
    df = df.rename(columns={"hour": "time"})
    df = df.sort_values(by="time")

    return df

host = st.secrets["INFLUX_HOST"]
org = st.secrets["INFLUX_ORG"]
token = st.secrets["INFLUX_TOKEN"]

client = InfluxDBClient3(host=host, token=token, org=org)

print(f'"Connected to InfluxDB at {host} with organization {org}"')

# Example usage
end_dt = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
start_dt = end_dt - timedelta(days=1)
start_date = start_dt.strftime('%Y-%m-%dT%H:%M:%SZ')
end_date = end_dt.strftime('%Y-%m-%dT%H:%M:%SZ')

key = "p_total"
df = query_data_from_influx(client, start_date, end_date, key)
# df = get_latest_data_from_influx(client, key)
print(df)