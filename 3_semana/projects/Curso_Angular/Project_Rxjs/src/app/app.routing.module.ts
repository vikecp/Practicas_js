import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { components } from './shared/components/index';
import { SkeletonComponent } from './layout/skeleton/skeleton.component';


const routes: Routes = [
    {
    path: '',
    component: SkeletonComponent
    }
];
@NgModule({
    imports: [RouterModule.forRoot(routes, {useHash: true})],
    exports: [RouterModule]

})
export class AppRoutingModule{

}