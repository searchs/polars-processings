import polars as pl
import datetime as dt
from loguru import logger


df = pl.DataFrame(
    {
        "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
        "birthdate": [
            dt.date(1997, 1, 10),
            dt.date(1985, 2, 15),
            dt.date(1983, 3, 22),
            dt.date(1981, 4, 30),
        ],
        "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
        "height": [1.56, 1.77, 1.65, 1.75],  # (m)
    }
)


def main():
    logger.info(df)
    logger.info(df.head(2))
    df.write_csv("data/output.csv")
    df_csv = pl.read_csv("data/output.csv", try_parse_dates=True)
    logger.info("""sumary_line""")
    logger.info(df_csv)
    result = df.select(
        pl.col("name"),
        pl.col("birthdate").dt.year().alias("birth_year"),
        pl.col("weight"),
        pl.col("height"),
        (pl.col("weight") / (pl.col("height") ** 2)).alias("bmi"),
    )
    logger.info(result)
    result_short = df.with_columns(
        birth_year=pl.col("birthdate").dt.year(),
        bmi=pl.col("weight") / (pl.col("height") ** 2),
    )
    logger.info(result_short)


if __name__ == "__main__":
    main()
