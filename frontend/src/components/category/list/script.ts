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
import _ from 'lodash';
import { AxiosError } from 'axios';
import CategoryEdit from '@/components/category/edit/CategoryEdit.vue';
import {
    Category,
    CategorySerachOption
} from '@/entity/category';


export default Vue.extend({
    data() {
        const option: CategorySerachOption = {
            q: ''
        }

        return {
            option
        };
    },
    mounted() {
        this.fetchCategories();
    },
    computed: {
        ...mapGetters('category', [
            'getCategories',
            'hasItems'
        ])
    },
    methods: {
        ...mapActions('category', [
            'fetchCategories',
            'delete'
        ]),
        /**
         * 商品カテゴリ検索
         */
        handleSearch(): void {
            this.fetchCategories(this.option);
        },
        /**
         * 検索オプションクリア
         */
        handleClearSerachOption(): void {
            this.$data.option.q = '';
        },
        /**
         * 商品カテゴリ新規作成
         */
        handleNew(): void {
            this._openEditModal();
        },
        /**
         * 商品カテゴリ編集
         * @param {Category} category 
         */
        handleEdit(category: Category): void {
            this._openEditModal(category.id);
        },
        /**
         * 商品カテゴリ削除
         * @param {Category} category 
         */
        handleDelete(category: Category): void {
            const message = `
                <div>『${category.name}』を削除しますか？<div>
                <small>＊削除したデータを元に戻すことはできません</small>`;
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
         * 編集モーダル表示
         * @param category  
         */
        _openEditModal(id?: number | null): void {
            const option: ModalConfig = {
                parent: this,
                component: CategoryEdit,
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
                        this.fetchCategories(this.option);
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
            let option: ToastConfig;
            this.delete(category.id)
                .then(() => {
                    option = {
                        message: '削除しました',
                        type: 'is-success'
                    };
                    this.$toast.open(option);
                    this.fetchCategories();
                })
                .catch((error: AxiosError) => {
                    let message = '削除できませんでした';

                    if (!_.isUndefined(error.response)) {
                        message = error.response.data.message;
                    }

                    option = {
                        message: message,
                        type: 'is-danger'
                    };

                    this.$toast.open(option);
                 });
        },
    }
});
