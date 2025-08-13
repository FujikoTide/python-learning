def main():
    item1 = Item("cat1", "animal1", Decimal("3.5"))
    item2 = Item("cat2", "animal2", Decimal("4.5"))
    item3 = Item("cat3", "animal3", Decimal("6.5"))

    print(item1)
    print(item2)
    print(item3)

    item1.change_item_name("cat5")


if __name__ == "__main__":
    main()
