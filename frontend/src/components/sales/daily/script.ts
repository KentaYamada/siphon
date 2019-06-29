import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import moment from 'moment';
import _ from 'lodash';
import DailySalesItem from '@/components/sales/daily/item/DailySalesItem.vue';
import { DailySalesSearchOption } from '@/entity/daily_sales';


/**
 * 日次売上一覧
 */
export default Vue.extend({
    data() {
        const params = this.$route.query;
        const salesDate = moment(
            params.sales_date as string,
            'YYYY-MM-DD'
        ).toDate();
        const option: DailySalesSearchOption = {
            sales_date: salesDate,
            time_from: null,
            time_to: null,
            q: ''
        };

        return {
            option
        };
    },
    mounted() {
        this.fetchDailySales(this.option);
    },
    components: {
        DailySalesItem
    },
    computed: {
        title(): string {
            const sales_date = moment(this.option.sales_date);
            return `${sales_date.format('YYYY年MM月DD日')}の売上`;
        },
        ...mapGetters('daily_sales', [
            'getDailySales',
            'hasItems'
        ])
    },
    methods: {
        /**
         * 売上検索
         */
        handleSearch(): void {
            this.fetchDailySales(this.option);
        },
        /**
         * 検索条件クリア
         */
        handleClearConditions(): void {
            this.$data.option.sales_date = null;
            this.$data.option.time_from = null;
            this.$data.option.time_to = null;
            this.$data.option.q = '';
        },
        ...mapActions('daily_sales', [
            'fetchDailySales'
        ])
    }
});
