/**
 * Item entity
 */
export interface Item {
    id?: number | null,
    category_id: number | null;
    name: string;
    unit_price: number;
}

/**
 * Item search option
 */
export interface ItemSearchOption {
    q: string;
    category_id?: number | null;
}
