import Vue from 'vue';
import {
    ModalConfig,
    ToastConfig,
    DialogConfig
} from 'buefy/types/components';
import { AxiosResponse } from 'axios';
import CategoryEdit from '@/components/category/edit/CategoryEdit.vue';
import Category from '@/entity/category';
import CategoryService from '@/api/category.service';


export default Vue.extend({
    data() {
        return {
            categories: [],
            errors: {}
        };
    },
    mounted() {
        this._fetch();
    },
    computed: {
        hasItems(): boolean {
            return this.categories.length > 0;
        },
    },
    methods: {
        /**
         * 商品カテゴリ検索
         */
        handleSearch(): void {
            this._fetch();
        },
        /**
         * 商品カテゴリ新規作成
         */
        handleNew(): void {
            this._openEditModal(new Category(null, ''));
        },
        /**
         * 商品カテゴリ編集
         * @param {Category} category 
         */
        handleEdit(category: Category): void {
            this._openEditModal(category);
        },
        /**
         * 商品カテゴリ削除
         * @param {Category} category 
         */
        handleDelete(category: Category): void {
            const message = `
                <div>${category.name}を削除しますか？<div>
                <small>Note:削除したデータを元に戻すことはできません</small>`;
            const option: DialogConfig = {
                title: '商品カテゴリ削除',
                message: message,
                confirmText: '削除',
                cancelText: '閉じる',
                hasIcon: true,
                type: 'is-danger',
                onConfirm: () => {
                    this._onDelete(category);
                }
            }
            this.$dialog.confirm(option);
        },
        /**
         * 商品カテゴリ取得
         */
        _fetch(): void {
            CategoryService.fetchCategories()
            .then((response: AxiosResponse<any>) => {
                console.log(response.data);
                this.categories = response.data.categories;
            })
            .catch((error: any) => {
                console.error(error);
            });
        },
        /**
         * 編集モーダル表示
         * @param category  
         */
        _openEditModal(category: Category): void {
            const option: ModalConfig = {
                parent: this,
                component: CategoryEdit,
                props: {
                    category: category
                },
                events: {
                    'save-success': (message: string) => {
                        const option: ToastConfig = {
                            message: message,
                            type:'is-success'
                        };
                        this.$toast.open(option);
                        this._fetch();
                    }
                }
            };
            this.$modal.open(option);
        },
        /**
         * 削除実行
         * @param category 
         */
        _onDelete(category: Category): void {
            CategoryService.deleteCategory(category.id)
                .then(() => {
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
    }
});

