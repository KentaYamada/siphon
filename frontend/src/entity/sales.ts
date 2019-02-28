import _ from 'lodash';
import Item from '@/entity/item';
import SalesItem from '@/entity/sales_item';

/**
 * 売上モデル
 */
export default class Sales {
    public total_price: number = 0;
    public discount_price: number = 0;
    public discount_rate: number = 0;
    public deposit: number = 0;
    public items: SalesItem[] = [];

    /**
     * 売上明細追加 or 明細商品数量追加
     * @param {Item} target
     */
    public increaseItem(target: Item): void {
        const index = _.findIndex(this.items, (item: SalesItem) => {
            return target.name === item.item_name;
        });

        if (index <= -1) {
            this.items.push(new SalesItem(
                target.name,
                target.price,
                1
            ));
        } else {
            this.items[index].amount += 1;
            this.items[index].calcSubtotal();
        }

        this._calcTotalPrice();
    }

    /**
     * 該当商品数を減らす or 行削除
     * @param {string} itemName
     */
    public decreaseItem(index: number): void {
        let item = this.items[index];
        const amount = item.amount - 1;

        if (amount < 1) {
            this.deleteItem(index);
        } else {
            item.amount -= 1;
            item.calcSubtotal();
        }

        this._calcTotalPrice();
    }

    /**
     * 売上明細削除
     * @param {SalesItem} target
     */
    public deleteItem(index: number): void {
        this.items.splice(index, 1);
        this._calcTotalPrice();
    }

    /**
     * 合計金額算出
     */
    private _calcTotalPrice(): void {
        // todo: discount
        this.total_price = _.sumBy(this.items, (item: SalesItem) => {
            return item.subtotal;
        });
    }
}

