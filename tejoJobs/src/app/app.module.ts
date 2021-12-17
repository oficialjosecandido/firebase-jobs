import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ServiceWorkerModule } from '@angular/service-worker';
import { environment } from '../environments/environment';
import { AngularFireModule } from '@angular/fire/compat';
import { AngularFirestoreModule } from '@angular/fire/compat/firestore';
import { AngularFireAuthModule } from '@angular/fire/compat/auth';
import { ProfilesComponent } from './components/profiles/profiles.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { DetailsComponent } from './components/profiles/details/details.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CreateComponent } from './components/profiles/create/create.component';
import { HttpClientModule } from '@angular/common/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { HomeComponent } from './components/home/home.component';


export const firebaseConfig = {
  apiKey: "AIzaSyAUBJVDXsm_FEbgRLj85kGu-v8ak9O6zD0",
  authDomain: "tejojobs-cb02d.firebaseapp.com",
  databaseURL: "https://tejojobs-cb02d-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "tejojobs-cb02d",
  storageBucket: "tejojobs-cb02d.appspot.com",
  messagingSenderId: "912087355725",
  appId: "1:912087355725:web:300c1e34c34c9c8ff3e704",
  measurementId: "G-MF6JHGHVND"
}

@NgModule({
  declarations: [
    AppComponent,
    ProfilesComponent,
    DashboardComponent,
    DetailsComponent,
    CreateComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    AngularFireModule.initializeApp(firebaseConfig),
    AngularFirestoreModule,
    AngularFireAuthModule,
    ServiceWorkerModule.register('ngsw-worker.js', {
      enabled: environment.production,
      // Register the ServiceWorker as soon as the app is stable
      // or after 30 seconds (whichever comes first).
      registrationStrategy: 'registerWhenStable:30000',
     
    }),
    NgbModule 
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
