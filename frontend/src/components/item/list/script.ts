import Vue from 'vue';
import Category from '@/entity/category';
import Item from '@/entity/item';
import ItemEdit from '@/components/item/edit/ItemEdit.vue';


export default Vue.extend({
    data() {
        const categories = Category.getDummyCategories();
        const items = Item.getDummyItems(1)

        return {
            categories,
            items
        };
    },
    computed: {
        hasItems(): boolean {
            return this.items.length > 0 ? true : false;
        }
    },
    methods: {
        handleNew(): void {
            this.$modal.open({
                parent: this,
                component: ItemEdit,
                hasModalCard: true,
                props: {
                    item: new Item()
                }
            });
        },
        handleEdit(item: Item): void {
            this.$modal.open({
                parent: this,
                component: ItemEdit,
                hasModalCard: true,
                props: {
                    item: item
                }
            });
        },
        handleDelete(item: Item): void {
            this.$dialog.confirm({
                title: '商品削除',
                message: `<div>${item.name}を削除しますか？<div><small>Note:削除したデータを元に戻すことはできません</small>`,
                confirmText: '削除',
                cancelText: '閉じる',
                hasIcon: true,
                type: 'is-danger'
            });
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

