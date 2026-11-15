import pandas as pd
import random
from datetime import datetime, timedelta

records = []

countries = [
    "India",
    "USA",
    "Russia",
    "China",
    "Germany",
    "Brazil",
    "Canada",
    "UK",
    "Japan",
    "Australia"
]

users = [
    "John","Alex","Raj","Amit","Smith",
    "David","Rohan","Mike","Sara","Priya",
    "Neha","Vikram","Kevin","Sophia","Emma"
]

statuses = [
    "Success",
    "Failed"
]

base_time = datetime(
    2026,1,1,8,0,0
)

for log_id in range(1,5001):

    user_id = random.randint(100,999)

    user_name = random.choice(users)

    country = random.choice(countries)

    ip = (
        f"{random.randint(1,255)}."
        f"{random.randint(1,255)}."
        f"{random.randint(1,255)}."
        f"{random.randint(1,255)}"
    )

    login_time = (
        base_time +
        timedelta(
            minutes=random.randint(
                1,100000
            )
        )
    )

    status = random.choices(
        statuses,
        weights=[80,20]
    )[0]

    records.append([
        log_id,
        user_id,
        user_name,
        country,
        ip,
        login_time,
        status
    ])

df = pd.DataFrame(
    records,
    columns=[
        "log_id",
        "user_id",
        "user_name",
        "country",
        "ip_address",
        "login_time",
        "status"
    ]
)

df.to_csv(
    "security_logs.csv",
    index=False
)

print(
    "Dataset created successfully."
)
print(
    "Total records:",
    len(df)
)

for i in range(5001,5201):

    records.append([
        i,
        777,
        "Attacker",
        "Russia",
        "175.23.12.2",
        datetime.now(),
        "Failed"
    ])