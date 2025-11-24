def cc():
    print("\n--- Calorie Calc ---")

    g = input("G (M/F): ").upper()
    a = int(input("A (yrs): "))
    w = float(input("W (kg): "))
    h = float(input("H (cm): "))

    print("\nAct:")
    print("1. Sed (no xrcise)")
    print("2. Lite (1–3/wk)")
    print("3. Mod (3–5/wk)")
    print("4. Act (6–7/wk)")
    lv = int(input("Pick (1–4): "))

    if g == 'M':
        b = 88.36
        bw = 13.4
        bh = 4.8
        ba = 5.7
        r = b + (bw * w)
        r = r + (bh * h)
        r = r - (ba * a)
    else:
        b = 447.6
        bw = 9.2
        bh = 3.1
        ba = 4.3
        r = b + (bw * w)
        r = r + (bh * h)
        r = r - (ba * a)

    ca = None
    if lv == 1:
        ca = r * 1.2
    elif lv == 2:
        ca = r * 1.375
    elif lv == 3:
        ca = r * 1.55
    else:
        ca = r * 1.725

    print("\n✨ R ✨")
    print("BMR:", round(r,2), "cal/d")
    print("Keep w:", round(ca,2), "cal/d")

    print("\nLose: -400~600cal")
    print("Gain: +400~600cal\n")

cc()
