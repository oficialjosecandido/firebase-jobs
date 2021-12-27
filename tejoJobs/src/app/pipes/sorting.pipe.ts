import { Pipe, PipeTransform } from '@angular/core';
import { orderBy } from 'lodash';

@Pipe({
  name: 'sorting'
})
export class SortingPipe implements PipeTransform {

  transform(array: any, sortBy: string, order?: string): any[] {
    const sortOrder = order ? order : 'desc'; // setting default ascending order
   
     return orderBy(array, [sortBy]);
     }
}
