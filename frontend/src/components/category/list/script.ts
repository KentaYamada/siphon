import Vue from 'vue';
import CategoryEdit from '@/components/category/edit/CategoryEdit.vue';
import Category from '@/entity/category';
import {
    ModalConfig,
    ToastConfig,
    DialogConfig
} from 'buefy/types/components';


export default Vue.extend({
    data() {
        return {
            categories: Category.getDummyCategories(),
            errors: {}
        };
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
        },
        /**
         * 商品カテゴリ新規作成
         */
        handleNew(): void {
            this._openEditModal(new Category(0, ''));
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
                    const option: ToastConfig = {
                        message: '削除しました。',
                        type: 'is-success'
                    };
                    this.$toast.open(option);
                }
            }
            this.$dialog.confirm(option);
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
    }
});

