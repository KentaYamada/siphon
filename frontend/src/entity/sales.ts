import SalesItem from '@/entity/sales_item';

/**
 * 値引種別
 */
export const enum DISCOUNT_TYPES {
    // 値引額
    PRICE = 1,
    // 値引率
    RATE
};

/**
 * 売上モデル
 */
export interface Sales {
    id?: number;
    total_price: number;
    discount_price: number;
    discount_rate: number;
    inclusive_tax?: number;
    exclusive_tax?: number;
    deposit: number;
    items: SalesItem[];
}
