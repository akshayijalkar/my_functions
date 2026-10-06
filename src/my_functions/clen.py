def clen(value):
    """
    Analyze a string and return grouped strings, integers, and floats.

    Rules
    -----
    Characters:
        Consecutive A-Z / a-z characters are grouped as strings.

    Integers:
        Consecutive digits are grouped as one integer.
        int_len is the total number of digits in all integer groups.

    Floats:
        A number containing a decimal point followed by digits
        is treated as one float.

        Examples:
            123.45 -> float
            .45    -> float
            123.   -> integer + ignored '.'
            . 45   -> ignored '.' + integer

    Spaces and special characters:
        They are ignored and are NOT included in char_len.

    Returns
    -------
    dict
        {
            "char_len": total length of all string groups,
            "int_len": total length of all integer groups,
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

        # -----------------------------------------------
        # STRING
        # -----------------------------------------------
        if value[i].isalpha():

            start = i

            while i < length and value[i].isalpha():
                i += 1

            strings.append(value[start:i])
            continue

        # -----------------------------------------------
        # NUMBER STARTING WITH A DIGIT
        # -----------------------------------------------
        if value[i].isdigit():

            start = i

            # Read complete integer part
            while i < length and value[i].isdigit():
                i += 1

            # Check whether this is a float
            #
            # 123.45 -> float
            # 123.   -> integer
            if (
                i < length
                and value[i] == "."
                and i + 1 < length
                and value[i + 1].isdigit()
            ):

                i += 1

                # Read decimal part
                while i < length and value[i].isdigit():
                    i += 1

                floats.append(value[start:i])

            else:
                integers.append(value[start:i])

            continue

        # -----------------------------------------------
        # FLOAT STARTING WITH "."
        # -----------------------------------------------
        #
        # .45 -> float
        # . 45 -> NOT float
        #
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

        # -----------------------------------------------
        # SPACE / SPECIAL CHARACTER
        # -----------------------------------------------
        #
        # Ignore it.
        #
        i += 1

    # -----------------------------------------------
    # FINAL VALUES
    # -----------------------------------------------

    return {
        "char_len": sum(len(item) for item in strings),
        "int_len": sum(len(item) for item in integers),
        "float": len(floats),

        "string": strings,
        "int": integers,
        "float_values": floats,
    }
