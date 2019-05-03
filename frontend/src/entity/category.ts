import { Item } from '@/entity/item';


export interface Category {
    id?: number;
    name: string;
    items?: Item[] | null;
}

export interface CategorySerachOption {
    q: string;
    with_items: boolean;
}
