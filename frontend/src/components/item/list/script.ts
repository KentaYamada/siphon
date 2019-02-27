import Vue from 'vue';
import Category from '@/entity/category';
import Item from '@/entity/item';
import ItemEdit from '@/components/item/edit/ItemEdit.vue';
import {
    ModalConfig,
    ToastConfig,
    DialogConfig
} from 'buefy/types/components';


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
        /**
         * 商品検索
         */
        handleSearch(): void {

        },
        /**
         * 商品新規登録
         */
        handleNew(): void {
            this._openEditModal(new Item(1, 1, 'item', 500));
        },
        /**
         * 商品編集
         * @param {Item} item
         */
        handleEdit(item: Item): void {
            this._openEditModal(item);
        },
        /**
         * 商品削除
         * @param {Item} item
         */
        handleDelete(item: Item): void {
            const message = `
                <div>${item.name}を削除しますか？<div>
                <small>Note:削除したデータを元に戻すことはできません</small>`;
            const option: DialogConfig = {
                title: '商品削除',
                message: message,
                confirmText: '削除',
                cancelText: '閉じる',
                hasIcon: true,
                type: 'is-danger',
                onConfirm: () => {
                    // todo: call delete api
                    this.deleteSuccess();
                    this.deleteFailed();
                }
            };
            this.$dialog.confirm(option);
        },
        deleteSuccess(): void {
            console.log('success');
        },
        deleteFailed(): void {
            console.log('failed');
        },
        /**
         * 編集モーダル表示
         * @param {Item} item
         */
        _openEditModal(item: Item): void {
            const option: ModalConfig = {
                parent: this,
                component: ItemEdit,
                hasModalCard: true,
                props: {
                    item: item
                },
                events: {
                    'save-success': () => {
                        const option: ToastConfig = {
                            message: '保存しました',
                            type:'is-success'
                        };
                        this.$toast.open(option);
                    }
                }
            };
            this.$modal.open(option);
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

