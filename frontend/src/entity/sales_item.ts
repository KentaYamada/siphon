/**
 * 売上明細モデル
 */
export default interface SalesItem {
    item_name: string;
    unit_price: number;
    quantity: number;
    subtotal: number;
}