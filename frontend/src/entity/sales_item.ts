export default class SalesItem {
    public item_name: string;
    public price: number;
    public amount: number;
    public subtotal: number;

    constructor(
        item_name: string='',
        price: number=0,
        amount: number=0) {
        this.item_name = item_name;
        this.price = price;
        this.amount = amount;
        this.subtotal = price * amount;
    }

    /**
     * 小計計算
     */
    public calcSubtotal(): void {
        this.subtotal = this.price * this.amount;
    }
}

