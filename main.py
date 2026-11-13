# برنامج قائمة المهام - مشروع ثناء الخامس
# Thanaa.codes

tasks = []

print("أهلاً فيك في برنامج قائمة مهام ثناء! 💜")
print("=" * 40)

while True:
    print("\nايش تبغى تسوي؟")
    print("1 - أضف مهمة جديدة")
    print("2 - شوف كل المهام")
    print("3 - احذف مهمة")
    print("4 - خروج")

    choice = input("\nاختر رقم: ")

    if choice == "1":
        task = input("اكتب المهمة: ")
        tasks.append(task)
        print(f"تم! أضفنا: {task} ✅")

    elif choice == "2":
        if len(tasks) == 0:
            print("ما عندك مهام لسه! ارتاحي 😴")
        else:
            print("\n--- مهامك اليوم ---")
            for i, t in enumerate(tasks, 1):
                print(f"{i} - {t}")

    elif choice == "3":
        if len(tasks) == 0:
            print("ما في شي نحذفه!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i} - {t}")
            num = int(input("اكتب رقم المهمة اللي تبغى تحذفها: "))
            deleted = tasks.pop(num - 1)
            print(f"حذفنا: {deleted} 🗑️")

    elif choice == "4":
        print("باي باي! شكراً انك استخدمت برنامج ثناء 💜")
        break

    else:
        print("اختر رقم من 1 الى 4 بس!")
