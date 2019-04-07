import { Sales } from '@/entity/sales';


/**
 * 日次売上モデル
 */
export interface DailySales extends Sales {
    sales_id: number;
    sales_date: Date;
    discount_unit: string;
    is_cancel: boolean;
}

/**
 * 日次売上検索オプション
 */
export interface DailySalesSearchOption {
    sales_date: Date | null,
    time_from: string,
    time_to: string,
    q: string
}
