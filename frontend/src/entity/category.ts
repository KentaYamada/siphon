import { Item, getDummyItems } from '@/entity/item';


export interface Category {
    id?: number;
    name: string;
    items?: Item[] | null;
}

export interface CategorySerachOption {
    q: string;
    with_items: boolean;
}

export const getDummyCashierPanel = (): Category[] =>  {
    let categories = [];

    for (let i = 1; i <= 10; i++) {
        let category: Category = {
            id: i,
            name: `Category${i}`
        };
        category.items = getDummyItems(i);
        categories.push(category);
    }

    return categories;
}
