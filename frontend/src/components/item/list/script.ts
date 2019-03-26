import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import {
    ModalConfig,
    ToastConfig,
    DialogConfig
} from 'buefy/types/components';
import ItemEdit from '@/components/item/edit/ItemEdit.vue';
import {
    Item,
    ItemSearchOption
} from '@/entity/item';


export default Vue.extend({
    data() {
        const option: ItemSearchOption = {
            q: '',
            category_id: null
        };

        return {
            option
        };
    },
    mounted() {
        this.fetchCategories();
        this.fetchItems();
    },
    computed: {
        ...mapGetters('category', [
            'getCategories'
        ]),
        ...mapGetters('item', [
            'getItems',
            'hasItems'
        ])
    },
    methods: {
        ...mapActions('category', [
            'fetchCategories'
        ]),
        ...mapActions('item', [
            'fetchItems',
            'delete'
        ]),
        /**
         * 商品検索
         */
        handleSearch(): void {
            this.fetchItems(this.option);
        },
        /**
         * 商品新規登録
         */
        handleNew(): void {
            this._openEditModal();
        },
        /**
         * 商品編集
         * @param item
         */
        handleEdit(item: Item): void {
            this._openEditModal(item.id);
        },
        /**
         * 商品削除
         * @param item
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
                    this._onDelete(item);
                }
            };
            this.$dialog.confirm(option);
        },
        /**
         * 編集モーダル表示
         * @param id
         */
        _openEditModal(id?: number | null): void {
            const option: ModalConfig = {
                parent: this,
                component: ItemEdit,
                hasModalCard: true,
                props: {
                    id: id
                },
                events: {
                    'save-success': (message: string) => {
                        const option: ToastConfig = {
                            message: message,
                            type:'is-success'
                        };
                        this.$toast.open(option);
                        this.fetchItems();
                    }
                }
            };
            this.$modal.open(option);
        },
        /**
         * 削除実行
         * @param item 
         */
        _onDelete(item: Item): void {
            this.delete(item.id)
                .then(() => {
                    const option: ToastConfig = {
                        message: '削除しました',
                        type: 'is-success'
                    };
                    this.$toast.open(option);
                    this.fetchItems();
                })
                .catch((error: any) => {
                });
        }
    },
    filters: {
        // todo: register global filter
        numberWithDelimiter(value: number): string {
            if (!value) {
                // todo: lodash or native??
                return '0';
            }
            return value.toString().replace(/(\d)(?=(\d{3})+$)/g, '$1,');
        }
    }
});
