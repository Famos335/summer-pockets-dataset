import sqlite3
from pathlib import Path


MAIN_DB = (
    Path(__file__).resolve().parent
    / "SummerPocketsRB_1771957083.197056_c0538fba-7b9a-4ac0-b0a6-511637015b17.sqlite"
)


def count_characters_in_source(db_path: Path) -> None:
    if not db_path.exists():
        raise FileNotFoundError(f"База не найдена: {db_path}")

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT
                COUNT(*) as row_count,
                SUM(LENGTH(source)) as total_chars,
                ROUND(AVG(LENGTH(source)), 2) as avg_chars,
                MIN(LENGTH(source)) as min_chars,
                MAX(LENGTH(source)) as max_chars
            FROM artificialtrans
            WHERE source IS NOT NULL
            """
        )
        result = cursor.fetchone()

        print("Результат подсчета символов")
        print("=" * 50)
        print(f"База:                   {db_path.name}")
        print(f"Количество строк:       {result[0]:,}")
        print(f"Всего символов:         {result[1]:,}")
        print(f"Среднее на строку:      {result[2]:.1f}")
        print(f"Самая короткая:         {result[3]} символов")
        print(f"Самая длинная:          {result[4]} символов")
        print("=" * 50)

        print("\nТоп-5 самых длинных строк:")
        cursor.execute(
            """
            SELECT id, LENGTH(source) as length
            FROM artificialtrans
            WHERE source IS NOT NULL
            ORDER BY length DESC
            LIMIT 5
            """
        )
        for row_id, length in cursor.fetchall():
            print(f"ID {row_id:3d} | {length:4d} символов")


if __name__ == "__main__":
    count_characters_in_source(MAIN_DB)
