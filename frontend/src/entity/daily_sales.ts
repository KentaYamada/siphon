import { Sales } from '@/entity/sales';

/**
 * 日次売上モデル
 */
export interface DailySales extends Sales {
    sales_date: Date;
    is_canceled: boolean;
    total_price: number;
    discount_unit: string;
    grand_total: number;
}

/**
 * 日次売上検索オプション
 */
export interface DailySalesSearchOption {
    sales_date?: string,
    time_from?: string,
    time_to?: string,
    q?: string
}
