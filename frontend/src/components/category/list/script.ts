import Vue from 'vue';
import CategoryEdit from '@/components/category/edit/CategoryEdit.vue';
import Category from '@/entity/category';


interface IEditModalOption {
    parent: any;
    component: any;
    hasModalCard: boolean;
    props: any;
}


export default Vue.extend({
    data() {
        return {
            categories: Category.getDummyCategories()
        };
    },
    computed: {
        hasItems(): boolean {
            return this.categories.length > 0;
        },
    },
    methods: {
        handleSearch(): void {
        },
        handleNew(): void {
            const option: any = {
                parent: this,
                component: CategoryEdit,
                hasModalCard: true,
                props: {
                    categpry: new Category(1, '')
                }
            };

            this.$modal.open(option);
        },
        handleEdit(category: Category): void {
            const option: IEditModalOption = {
                parent: this,
                component: CategoryEdit,
                hasModalCard: true,
                props: {
                    category: category
                }
            };

            this.$modal.open(option);
        },
        handleDelete(category: Category): void {
            // todo: 削除用モーダル
            this.$dialog.confirm({
                title: '商品カテゴリ削除',
                message: `<div>${category.name}を削除しますか？<div><small>Note:削除したデータを元に戻すことはできません</small>`,
                confirmText: '削除',
                cancelText: '閉じる',
                hasIcon: true,
                type: 'is-danger'
            });
        },
        handleSaveSuccess(): void {
            console.log('success');
        }
    }
});

