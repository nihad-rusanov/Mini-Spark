def parse_query(query):
    # Örnek: SELECT name FROM products WHERE price > 500
    parts = query.lower().split("where")
    select_part = parts[0].strip()
    condition_part = parts[1].strip() if len(parts) > 1 else None

    select_column = select_part.replace("select", "").replace("from products", "").strip()

    if condition_part:
        # Örnek: "price > 500"
        col, op, val = condition_part.split()
        val = float(val) if "." in val else int(val)

        def condition(row, header):
            idx = header.index(col)
            return eval(f"float(row[idx]) {op} {val}")

    else:
        condition = lambda row, header: True

    def transformer(header):
        select_idx = header.index(select_column)
        return (
            lambda row: row[select_idx],
            lambda row: condition(row, header)
        )

    return transformer
