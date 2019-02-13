/**
 * Item entity
 */
export default class Item {
    public id: number;
    public categoryId: number;
    public name: string;
    public price: number;

    constructor(id: number, categoryId: number, name: string, price: number) {
        this.id = id;
        this.categoryId = categoryId;
        this.name = name;
        this.price = price;
    }

    public static getDummyItems(categoryId: number): Item[] {
        let list = [];

        for (let i = 1; i <= 30; i++) {
            list.push(new Item(i, categoryId, 'Item' + i, i * 100));
        }

        return list;
    }
}

