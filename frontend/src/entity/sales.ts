import _ from 'lodash';
import { Item } from '@/entity/item';
import { SalesItem } from '@/entity/sales_item';

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
export class Sales {
    public total_price: number = 0;
    public discount_price: number = 0;
    public discount_rate: number = 0;
    public inclusive_tax: number = 0;
    public exclusive_tax: number = 0;
    public deposit: number = 0;
    public items: SalesItem[] = [];

    /**
     * 売上明細追加 or 明細商品数量追加
     * @param {Item} target
     */
    public increaseItem(target: Item, discountType: DISCOUNT_TYPES): void {
        const index = _.findIndex(this.items, (item: SalesItem) => {
            return target.name === item.item_name;
        });

        if (index <= -1) {
            this.items.push(new SalesItem(
                target.name,
                target.unit_price,
                1
            ));
        } else {
            this.items[index].amount += 1;
            this.items[index].calcSubtotal();
        }

        this.calcTotalPrice(discountType);
    }

    /**
     * 該当商品数を減らす or 行削除
     * @param {string} itemName
     * @param {DISCOUNT_TYPES} discountType
     */
    public decreaseItem(itemName: string, discountType: DISCOUNT_TYPES): void {
        const index = _.findIndex(this.items, (item: SalesItem) => {
            return itemName === item.item_name;
        });

        if (index > -1) {
            let item = this.items[index];
    
            if (item.amount > 1) {
                item.amount -= 1;
                item.calcSubtotal();
                this.calcTotalPrice(discountType);
            } else {
                this.deleteItem(index, discountType);
            }
        }
    }

    /**
     * 売上明細削除
     * @param {SalesItem} target
     * @param {DISCOUNT_TYPES} discountType
     */
    public deleteItem(index: number, discountType: DISCOUNT_TYPES): void {
        this.items.splice(index, 1);
        this.calcTotalPrice(discountType);
    }

    /**
     * 合計金額算出
     * @param {DISCOUNT_TYPES} discountType
     */
    public calcTotalPrice(discountType: DISCOUNT_TYPES): void {
        this.total_price = _.sumBy(this.items, (item: SalesItem) => {
            return item.subtotal;
        });

        switch (discountType) {
            case DISCOUNT_TYPES.PRICE:
                // 値引額
                this.total_price -= this.discount_price;
                break;
            case DISCOUNT_TYPES.RATE:
                // 値引率
                this.total_price = this.total_price * (1 - this.discount_rate / 100);
                break;
            default:
                // do nothing
                break;
        }
    }
}

