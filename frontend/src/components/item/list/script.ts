import Vue from 'vue';
import {
    ModalConfig,
    ToastConfig,
    DialogConfig
} from 'buefy/types/components';
import { AxiosResponse } from 'axios';
import CategoryService from '@/api/category.service';
import {Item, ItemSearchOption } from '@/entity/item';
import ItemEdit from '@/components/item/edit/ItemEdit.vue';
import ItemService from '@/api/item.service';


export default Vue.extend({
    data() {
        return {
            categories: [],
            items: []
        };
    },
    mounted() {
        CategoryService.fetchCategories()
            .then((response: AxiosResponse<any>) => {
                this.categories = response.data.categories;
            })
            .catch((error: any) => {
                console.error(error);
            });
        this._fetch();
    },
    props: {
        q: {
            type: String
        },
        category_id: {
            type: Number
        }
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
            const newItem: Item = {
                id: null,
                category_id: null,
                name: '',
                unit_price: 0
            };
            this._openEditModal(newItem);
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
                    this._onDelete(item);
                }
            };
            this.$dialog.confirm(option);
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
                    'save-success': (message: string) => {
                        const option: ToastConfig = {
                            message: message,
                            type:'is-success'
                        };
                        this.$toast.open(option);
                    }
                }
            };
            this.$modal.open(option);
        },
        _fetch(): void {
            const option: ItemSearchOption = {
                category_id: this.category_id,
                q: this.q
            };
            ItemService.fetchItems(option)
                .then((response: AxiosResponse<any>) => {
                    console.log(response);
                    this.items = response.data.items;
                })
                .catch((error: any) => {
                    console.log(error);
                });
        },
        _onDelete(item: Item): void {
            ItemService.deleteItem(item.id)
                .then((response: AxiosResponse<any>) => {
                    const option: ToastConfig = {
                        message: '削除しました',
                        type: 'is-success'
                    };
                    this.$toast.open(option);
                    this._fetch();
                })
                .catch((error: any) => {
                });
        }
    },
    filters: {
        numberWithDelimiter(value: number): string {
            if (!value) {
                // todo: lodash or native??
                return '0';
            }
            return value.toString().replace(/(\d)(?=(\d{3})+$)/g, '$1,');
        }
    }
});
