export class SalesItem {
    public item_name: string;
    public unit_price: number;
    public amount: number;
    public subtotal: number;

    constructor(
        item_name: string='',
        price: number=0,
        amount: number=0) {
        this.item_name = item_name;
        this.unit_price = price;
        this.amount = amount;
        this.subtotal = price * amount;
    }

    /**
     * 小計計算
     */
    public calcSubtotal(): void {
        this.subtotal = this.unit_price * this.amount;
    }
}

