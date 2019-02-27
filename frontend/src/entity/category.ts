import Item from '@/entity/item';


export default class Category {
    public id: number | null = null;
    public name: string | null = null;
    public items: Item[];

    constructor(id: number, name: string, items: Item[]=[]) {
        this.id = id;
        this.name = name;
        this.items = items;
    }

    public static getDummyCategories(): Category[] {
        let list = [];

        for (let i = 1; i <= 10; i++) {
            list.push(new Category(i, 'Category ' + i));
        }

        return list;
    }

    public static getDummyCashierPanel(): Category[] {
        let categories = [];

        for (let i = 1; i <= 10; i++) {
            let category = new Category(i, `Category${i}`);
            category.items = Item.getDummyItems(i);
            categories.push(category);
        }

        console.log(categories);
        return categories;
    }
}

