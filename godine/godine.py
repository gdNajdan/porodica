while True:
    godiste_mame = (input("kada se mama rodila? "))
    d1 = (input("koliko prvo dete ima godina? "))
    d2 = (input("koliko drugo dete ima godina? "))
    try:
        brojgodiste_mame = int(godiste_mame)
        brojd1 = int(d1)
        brojd2 = int(d2)
        godine_mame = 2024 - godiste_mame
        rodilad1 = godine_mame - d1
        rodilad2 = godine_mame - d2
        print("mama je imala ", rodilad1, "godina kada je rodila prvo dete")
        print("mama je imala ", rodilad2, "godina kada je rodila drugo dete")
        break
    except:
        print("niste uneli brojeve.")