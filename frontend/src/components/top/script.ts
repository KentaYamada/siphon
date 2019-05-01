import Vue from 'vue';
import moment from 'moment';
import {
    mapActions,
    mapGetters
} from 'vuex';
import { DashboardSearchOption } from '@/entity/dashboard';


export default Vue.extend({
    data() {
        const option: DashboardSearchOption = {
            target: moment().toDate()
        };

        return {
            option
        };
    },
    mounted() {
        this.fetchDashboardData(this.option);
    },
    computed: {
        ...mapGetters('dashboard', [
            'getMonthlySales',
            'getPopularItems',
            'hasMonthlySales',
            'hasPopularItems'
        ]),
        currentMonth(): string {
            return moment(this.option.target).format('YYYY年MM月');
        },
    },
    methods: {
        ...mapActions('dashboard', [
            'fetchDashboardData'
        ]),
        /**
         * 前年月のデータ取得
         */
        handlePrevMonth(): void {
            this.option.target = moment(this.option.target).add(-1, 'M').toDate();
            this.fetchDashboardData(this.option);
        },
        /**
         * 次年月のデータ取得
         */
        handleNextMonth(): void {
            this.option.target = moment(this.option.target, 'YYYY-MM-DD').add(1, 'M').toDate();
            this.fetchDashboardData(this.option);
        }
    },
    filters: {
        numberWithDelimiter(value: number): string {
            if (!value) {
                return '0';
            }
            return value.toString().replace(/(\d)(?=(\d{3})+$)/g, '$1,');
        }
    }
});