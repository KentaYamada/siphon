export const getDummyItems = (categoryId: number) => {
    let list = [];

    for (let i = 1; i <= 30; i++) {
        const item: Item = {
            id: i,
            category_id: categoryId,
            name: `Item ${i}`,
            unit_price: i * 100
        };
        list.push(item);
    }

    return list;
}

/**
 * Item entity
 */
export interface Item {
    id: number | null,
    category_id: number | null;
    name: string;
    unit_price: number;
}

/**
 * Item search option interface
 */
export interface ItemSearchOption {
    q: string;
    category_id: number | null;
}
