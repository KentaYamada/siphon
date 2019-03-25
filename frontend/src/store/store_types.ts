import { Sales } from '@/entity/sales';
import { Category } from '@/entity/category';
import { Item } from  '@/entity/item';
import { User } from  '@/entity/user';

/** Cashier state */
export interface CashierState {
    sales: Sales
}

/** Category state */
export interface CategoryState {
    categories: Category[];
}

/** Item state */
export interface ItemState {
    items: Item[];
}

/** User state */
export interface UserState {
    users: User[];
}
