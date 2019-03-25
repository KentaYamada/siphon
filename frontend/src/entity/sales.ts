import SalesItem from '@/entity/sales_item';

/**
 * 値引種別
 */
export const enum DISCOUNT_TYPES {
    // 値引額
    PRICE,
    // 値引率
    RATE
};

/**
 * 売上モデル
 */
export interface Sales {
    total_price: number;
    discount_price: number;
    discount_rate: number;
    inclusive_tax: number | null;
    exclusive_tax: number | null;
    deposit: number;
    items: SalesItem[];
}
