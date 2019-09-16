import { TAX_OPTIONS } from '@/entity/tax_rate';
import { Item } from './item';


/**
 * 売上明細モデル
 */
export interface SalesItem {
    name: string;
    unit_price: number;
    quantity: number;
    subtotal: number;
    tax_option: TAX_OPTIONS;
};

export interface TargetItem {
    item: Item | SalesItem;
    tax_option: TAX_OPTIONS;
}