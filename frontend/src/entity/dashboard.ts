/**
 * 月間売上
 */
export interface MonthlySales {
    sales_date: number;
    sales_day: Date | null;
    amount: number | null;
    is_holiday: boolean;
    is_satarday: boolean;
}

/**
 * 人気商品
 */
export interface PopularItem {
    rank_no: number;
    item_name: string;
}

/**
 * ダッシュボード検索オプション
 */
export interface DashboardSearchOption {
    target: Date;
}
