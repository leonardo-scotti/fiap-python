def calculate_mean(temps):
    media = (temps[0] + temps[1] + temps[2] + temps[3]) / 4;
    return media

def message_output(sala, media, criticos):
    print(f"\nSala {sala}\n"
          f"Média: {media}\n"
          f"Registros críticos: {criticos}")

def count_critics(temps):
    critcs = 0
    for temp in temps:
        if (temp >= 33):
            critcs += 1

    return critcs


temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

for i in range(len(temperaturas)):

    mean = calculate_mean(temperaturas[i])
    critcs = count_critics(temperaturas[i])

    message_output(i, mean, critcs)
