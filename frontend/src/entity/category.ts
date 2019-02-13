
export default class Category {
    public id: number;
    public name: string;

    constructor(id: number, name: string) {
        this.id = id;
        this.name = name;
    }

    public static getDummyCategories(): Category[] {
        let list = [];

        for (let i = 1; i <= 10; i++) {
            list.push(new Category(i, 'Category ' + i));
        }

        return list;
    }
}

