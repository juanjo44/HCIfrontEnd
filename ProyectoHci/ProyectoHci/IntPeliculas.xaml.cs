﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace ProyectoHci
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class IntPeliculas : ContentPage
    {
        public IntPeliculas()
        {
            InitializeComponent();
        }

        private async void volver(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new Peliculas());
        }

        private async void irGeneros(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new Generos());
        }
    }
}