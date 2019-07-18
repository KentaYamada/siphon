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
    canceled: boolean;
}

/**
 * 日次売上検索オプション
 */
export interface DailySalesSearchOption {
    sales_date: Date,
    time_from: Date | null,
    time_to: Date | null,
    q?: string
}
