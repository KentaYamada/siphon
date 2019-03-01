import Item from '@/entity/item';


export default class Category {
    public id: number | null;
    public name: string | null;
    public items: Item[] | null;

    constructor(
        id: number | null,
        name: string | null,
        items: Item[] | null = null) {
        this.id = id;
        this.name = name;
        this.items = items;
    }

    public static getDummyCashierPanel(): Category[] {
        let categories = [];

        for (let i = 1; i <= 10; i++) {
            let category = new Category(i, `Category${i}`);
            category.items = Item.getDummyItems(i);
            categories.push(category);
        }

        return categories;
    }
}

export interface CategorySerachOption {
    q: string;
}