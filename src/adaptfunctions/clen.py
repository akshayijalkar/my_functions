def clen(value):
    """
    Analyze a string and separate:
    - alphabetic strings
    - integers
    - floats

    Also prints string, int, and float_values
    in tabular column format.

    Returns
    -------
    dict
        {
            "char_len": total alphabetic character count,
            "int_len": total integer digit count,
            "float": number of float groups,
            "string": list of string groups,
            "int": list of integer groups,
            "float_values": list of float groups
        }
    """

    if not isinstance(value, str):
        raise TypeError("clen() expects a string")

    strings = []
    integers = []
    floats = []

    i = 0
    length = len(value)

    while i < length:

        # -----------------------------
        # STRING
        # -----------------------------
        if value[i].isalpha():

            start = i

            while i < length and value[i].isalpha():
                i += 1

            strings.append(value[start:i])
            continue

        # -----------------------------
        # NUMBER STARTING WITH DIGIT
        # -----------------------------
        if value[i].isdigit():

            start = i

            while i < length and value[i].isdigit():
                i += 1

            # Check for float
            if (
                i < length
                and value[i] == "."
                and i + 1 < length
                and value[i + 1].isdigit()
            ):

                i += 1

                while i < length and value[i].isdigit():
                    i += 1

                floats.append(value[start:i])

            else:
                integers.append(value[start:i])

            continue

        # -----------------------------
        # FLOAT STARTING WITH "."
        # -----------------------------
        if (
            value[i] == "."
            and i + 1 < length
            and value[i + 1].isdigit()
        ):

            start = i
            i += 1

            while i < length and value[i].isdigit():
                i += 1

            floats.append(value[start:i])
            continue

        # Ignore special characters/spaces
        i += 1

    # -----------------------------
    # RESULT
    # -----------------------------
    result = {
        "char_len": sum(len(item) for item in strings),
        "int_len": sum(len(item) for item in integers),
        "float": len(floats),
        "string": strings,
        "int": integers,
        "float_values": floats,
    }

    # -----------------------------
    # LENGTH INFORMATION
    # -----------------------------
    print(f"char_len : {result['char_len']}")
    print(f"int_len  : {result['int_len']}")
    print(f"float    : {result['float']}")

    print()

    # -----------------------------
    # TABLE
    # -----------------------------
    print(f"{'string':<20}{'int':<20}{'float_values':<20}")
    print("-" * 60)

    max_rows = max(
        len(strings),
        len(integers),
        len(floats),
        1
    )

    for index in range(max_rows):

        string_value = strings[index] if index < len(strings) else ""
        int_value = integers[index] if index < len(integers) else ""
        float_value = floats[index] if index < len(floats) else ""

        print(
            f"{string_value:<20}"
            f"{int_value:<20}"
            f"{float_value:<20}"
        )

    return result
