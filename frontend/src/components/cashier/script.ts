import Vue from 'vue';
import Sales from '@/entity/sales';
import SalesItem from '@/entity/sales_item';
import _ from 'lodash';


function getItems() {
    let items = [];
    let index = 1;

    for (let i = 0; i < 10; i++) {
        let row = [];

        for(let j = 0; j < 3; j++) {
            row.push({
                name: 'Item ' + index,
                price: index * 100
            });
            index++;
        }

        items.push(row);
    }

    return items;
}

function getDummySalesItems(): SalesItem[] {
    let list = [];

    for (let i = 1; i <= 10; i++) {
        list.push(new SalesItem(
            `Item ${i}`,
            500,
            i,
            500 * i
        ));
    }

    return list;
}
export default Vue.extend({
    data() {
        const items = getItems();
        const salesItems = getDummySalesItems();

        return {
            sales: new Sales(0, 0, 0, 0),
            items: items,
            sales_items: salesItems
        };
    },
    methods: {
        handleIncreaseItem(selectedItem: SalesItem): void {
            const target = _.find(this.sales.items, (item: SalesItem) => {
                return item.item_name === selectedItem.item_name;
            });

            if (!_.isUndefined(target)) {
            } else {
            }
            //if (this._.isUndefined(target)) {
            //   this.sales.items.push(new SalesItem(
            //       selectedItem.name,
            //       selectedItem.price,
            //       1,
            //       selectedItem.price,
            //   ));
            //} else {
            //    target.amount += 1;
            //}
        },
        handleDecreaseItem(selectedItem: SalesItem): void {
            //const target = this._.find(this.sales.items, function(item) {
            //    return selectedItem.name === item.item;
            //});

            //if (!this._.isUndefined(target)) {
            //    if (--target.amount > 0) {
            //        target.amount -= 1;
            //    } else {
            //        this.sales.items = this._.reject(this.sales.items, function(item) {
            //            return selectedItem === item.item;
            //        });
            //    }
            //}
        },
        handleDeleteItem(selectedItem: SalesItem): void {
            //const target = this._.find(this.sales.items, function(item) {
            //    return selectedItem.name === item.item;
            //});
            //let option = {
            //    message: '',
            //    type: ''
            //};

            //if (!this._.isUndefined(target)) {
            //    this.sales.items = this._.reject(this.sales.items, function(item) {
            //        return selectedItem === item.item;
            //    });
            //    option.message = '削除しました';
            //    option.type = 'is-success';
            //} else {
            //    option.message = '削除する商品が見つかりませんでした';
            //    option.type = 'is-danger';
            //}

            //this.$toast.open(option);
        },
        handleChangeDiscountMode(): void {
        },
        handleSave(): void {
        },
        handleConfirmDeleteItem(): void {
            const option = {
                title: '商品削除',
                message: '選択した商品を削除します。よろしいですか？',
                confirmText: '削除',
                cancelText: '閉じる',
                type: 'is-danger',
                onConfirm: () => {
                    const option = {
                        message: '削除しました。',
                        type: 'is-success'
                    };
                    this.$toast.open(option);
                }
            };
            this.$dialog.confirm(option);
        }
    },
    filters: {
        numberWithDelimiter(value: number): string {
            if (!value) {
                // todo: lodash or native??
                return '';
            }
            return value.toString().replace(/(\d)(?=(\d{3})+$)/g, '$1,');
        }
    }
});

