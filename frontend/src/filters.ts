import _ from 'lodash';


export default {
    /**
     * 数値を3桁カンマ区切りでフォーマット
     * @param value
     * @param defaultValue
     */
    toNumWithDelimiter: (value: number, defaultValue?: string): string => {
        const d = _.isUndefined(defaultValue) ? '0' : defaultValue;
        return value ? value.toLocaleString() : d;
    }
}