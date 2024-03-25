for i in range(1,10):
    if i == 3:
        print(f"skipping {i}")
        continue
    elif i == 7:
        print(f"reached {i} breaking loop")
        break
    print(i)